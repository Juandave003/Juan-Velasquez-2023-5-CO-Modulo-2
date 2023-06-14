from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy1 = Enemy(ENEMY_1, 40, 60, [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 1000], 20, 5, 1, 'left', 30)
            self.enemies.append(enemy1)
            enemy2 = Enemy(ENEMY_2, 60, 80, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 40, 3, 2, 'right', 50)
            self.enemies.append(enemy2)