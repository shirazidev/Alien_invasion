import sys
import json
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from time import sleep
from game_stats import GameStats
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set up the game screen to be fullscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion By ShiraziDEV")

        # Create an instance to store game statistics and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create an instance of the ship, and groups for bullets and aliens
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create the fleet of aliens
        self._create_fleet()

        self.easy_button = Button(self, "Easy", (100, 100))
        self.medium_button = Button(self, "Medium", (100, 200))
        self.hard_button = Button(self, "Hard", (100, 300))
        self.play_button = Button(self, "Play", (100, 400))

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._check_difficulty_button()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    # Inside the _check_difficulty_button method of AlienInvasion class

    def _check_difficulty_button(self):
        """Check for difficulty selection."""
        if not self.stats.game_active:  # Only allow changing difficulty if the game is not active
            mouse_pos = pygame.mouse.get_pos()
            # Reset button colors
            self.easy_button.set_selected_color(False)
            self.medium_button.set_selected_color(False)
            self.hard_button.set_selected_color(False)
            # Check which button is clicked and set its color to red
            if self.easy_button.rect.collidepoint(mouse_pos):
                self.easy_button.set_selected_color(True)
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    self.settings.difficulty = "easy"
                    self.settings.set_difficulty()
            elif self.medium_button.rect.collidepoint(mouse_pos):
                self.medium_button.set_selected_color(True)
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    self.settings.difficulty = "medium"
                    self.settings.set_difficulty()
            elif self.hard_button.rect.collidepoint(mouse_pos):
                self.hard_button.set_selected_color(True)
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    self.settings.difficulty = "hard"
                    self.settings.set_difficulty()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score(self.stats.high_score)  # Save high score when quitting
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                # Check difficulty button clicks
                self._check_difficulty_button()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.stats.save_high_score(self.stats.high_score)  # Save high score when quitting
                    sys.exit()
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            # تمرین 3-1
        elif event.key == pygame.K_p:  # Start the game when 'P' is pressed
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _save_high_score(self):
        """Save the high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.stats.save_high_score(self.stats.high_score)
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # Update the score for each collision and check for a new high score
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # If all aliens are destroyed, create a new fleet and increase the speed
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase the level
            self.stats.level += 1
            self.sb.prep_level()

    # Inside the _update_screen method of AlienInvasion class

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # Draw the buttons
        if not self.stats.game_active:
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            self.play_button.draw_button()
        else:
            # Show only the selected difficulty button
            if self.settings.difficulty == "easy":
                self.easy_button.draw_button()
            elif self.settings.difficulty == "medium":
                self.medium_button.draw_button()
            elif self.settings.difficulty == "hard":
                self.hard_button.draw_button()
            # Draw the play button if the game is inactive
            if not self.stats.game_active:
                self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement the number of ships left and update the scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Clear the aliens and bullets and create a new fleet
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            # Pause the game briefly
            sleep(0.5)
        else:
            # End the game if no ships are left and make the mouse visible
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            # Check if the current score is higher than the high score
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score
                # Save the new high score
                self.stats.save_high_score(self.stats.high_score)  # Save high score here

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            # Set the buttons to None to make them disappear
            # self.easy_button = None
            # self.medium_button = None
            # self.hard_button = None
            # self.play_button = None

    # 3-1
    def _start_game(self):
        """Start a new game when the player presses 'P' or clicks Play."""
        # Reset the game settings and statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True

        # Prepare the scoreboard
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_high_score()
        self.sb.prep_ships()

        # Clear the aliens and bullets, create a new fleet, and center the ship
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Create an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
