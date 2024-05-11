import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats


class AlienInvasion:
    # managing game assets

    def __init__(self):
        # initalize the game
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion By ShiraziDEV")
        # create an instance to store game stats
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        # game loop
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()

            # make recent drawn screen display
            pygame.display.flip()

    def _check_events(self):
        # respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # move the ship to right

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # move the ship to right

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # create a new bullet and add it to bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # get rid of bullets out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # check for bullet and alien collisions
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # check for any bullets that have hit aliens
        # if so get rid of the bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine number of rows of alien that fits on screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        # create fleet of aliens and find number of aliens in the row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # create alien and place it in row
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        # update pos of all aliens in the fleet
        # check if fleet os at an edge
        # then update the positions of all aliens in fleet
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        # respond if any alien reach edges
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        # drop entire fleet and change the fleet's dir
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _ship_hit(self):
        # respond to ship being hit by an alien
            # decrement shi[s_left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # get rid of ant remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        # check if any aliens have reached the bottom of screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>= screen_rect.bottom:
            # treat this same as if the ship got hit
                self._ship_hit()
                break

if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
