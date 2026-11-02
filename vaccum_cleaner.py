class SimpleReflexVacuumAgent:
    def __init__(self):
        self.location = 'A'

    def sense_and_act(self, status):
        """Maps current room state/status to an action."""
        if status == 'Dirty':
            return 'Suck'
        elif self.location == 'A':
            return 'Right'
        elif self.location == 'B':
            return 'Left'

    def update_location(self, action):
        """Updates internal position tracking after movement."""
        if action == 'Right':
            self.location = 'B'
        elif action == 'Left':
            self.location = 'A'


class VacuumEnvironment:
    def __init__(self, state_dict):
        self.states = state_dict

    def run_simulation(self, agent, steps=4):
        print(f"Initial Environment State: {self.states}")
        print(f"Agent starts at Location: {agent.location}\n")

        for step in range(1, steps + 1):
            current_status = self.states[agent.location]
            action = agent.sense_and_act(current_status)
            
            print(f"Step {step}: At {agent.location}, Status: {current_status} -> Action: {action}")
            
            if action == 'Suck':
                self.states[agent.location] = 'Clean'
            else:
                agent.update_location(action)
                
        print(f"\nFinal Environment State: {self.states}")
        
initial_state = {'A': 'Dirty', 'B': 'Dirty'}
my_agent = SimpleReflexVacuumAgent()
sim = VacuumEnvironment(initial_state)
sim.run_simulation(my_agent, steps=4)
