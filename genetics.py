from random import choice, random


class GeneticsManeger:
    def __init__(
        self,
        population_size: int,
        creature_generator,
        environment_generator
    ) -> None:
        self.population_size = population_size
        self.population = [creature_generator() for _ in range(self.population_size)]
        self.environment = environment_generator()
        self.evaluate_population()
    
    def evaluate_population(self):
        self.environment.reached_target = 0
        [self.environment.evaluate(creature) for creature in self.population]
    
    def reproduce(self):
        tmp = []
        [tmp.extend([creature]*int(creature.score())*100) for creature in self.population]

        new_population = []
        for _ in range(self.population_size):
            new_population.append(choice(self.population).reproduce(choice(self.population)))
        
        for creature in new_population:
            if random() < 0.001:
                creature.mutate()
        self.population = new_population
        self.evaluate_population()
    
    def draw(self, surface):
        # m = max(self.population, key=lambda x: x.score())
        # m.draw(surface)
        [creature.draw(surface) for creature in self.population]
        self.environment.draw(surface)