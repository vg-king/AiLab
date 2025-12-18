# Vacuum Cleaner World - State Space Search
# Actions: L (Left), R (Right), S (Suck)
# States: (location, left_dirty, right_dirty)

class VacuumWorld:
    def __init__(self):
        # Location: 0=Left, 1=Right
        # Dirty: 0=Clean, 1=Dirty
        self.location = 0
        self.left_dirty = 1
        self.right_dirty = 1
        self.actions_taken = []
    
    def reset(self, loc=0, left=1, right=1):
        """Reset to initial state"""
        self.location = loc
        self.left_dirty = left
        self.right_dirty = right
        self.actions_taken = []
    
    def get_state(self):
        """Return current state as tuple"""
        return (self.location, self.left_dirty, self.right_dirty)
    
    def is_clean(self):
        """Check if both rooms are clean"""
        return self.left_dirty == 0 and self.right_dirty == 0
    
    def get_possible_actions(self):
        """Return list of valid actions"""
        actions = []
        if self.location == 0:  # In left room
            actions.append('R')  # Can move right
            if self.left_dirty == 1:
                actions.append('S')  # Can suck if dirty
        else:  # In right room
            actions.append('L')  # Can move left
            if self.right_dirty == 1:
                actions.append('S')  # Can suck if dirty
        return actions
    
    def perform_action(self, action):
        """Perform action and return success"""
        if action not in self.get_possible_actions():
            return False
        
        if action == 'L':
            self.location = 0
        elif action == 'R':
            self.location = 1
        elif action == 'S':
            if self.location == 0:
                self.left_dirty = 0
            else:
                self.right_dirty = 0
        
        self.actions_taken.append(action)
        return True
    
    def display(self):
        """Display current state"""
        left_symbol = '[D]' if self.left_dirty else '[C]'
        right_symbol = '[D]' if self.right_dirty else '[C]'
        
        if self.location == 0:
            left_symbol = f'(V){left_symbol}'
        else:
            right_symbol = f'(V){right_symbol}'
        
        print(f"  {left_symbol} --- {right_symbol}")
        print(f"  Left        Right")


def generate_state_space():
    """Generate complete state space graph"""
    print("="*60)
    print("VACUUM WORLD - COMPLETE STATE SPACE")
    print("="*60)
    print("\nStates: (Location, Left_Status, Right_Status)")
    print("Location: 0=Left, 1=Right")
    print("Status: 0=Clean, 1=Dirty")
    print("\nActions: L=Move Left, R=Move Right, S=Suck\n")
    print("-"*60)
    
    # All possible states: 2 locations × 2 left states × 2 right states = 8 states
    states = []
    for loc in [0, 1]:
        for left in [0, 1]:
            for right in [0, 1]:
                states.append((loc, left, right))
    
    # Print state space with transitions
    state_names = {
        (0, 0, 0): "State 1: Left, Clean, Clean",
        (0, 0, 1): "State 2: Left, Clean, Dirty",
        (0, 1, 0): "State 3: Left, Dirty, Clean",
        (0, 1, 1): "State 4: Left, Dirty, Dirty",
        (1, 0, 0): "State 5: Right, Clean, Clean",
        (1, 0, 1): "State 6: Right, Clean, Dirty",
        (1, 1, 0): "State 7: Right, Dirty, Clean",
        (1, 1, 1): "State 8: Right, Dirty, Dirty",
    }
    
    for state in states:
        loc, left, right = state
        print(f"\n{state_names[state]}")
        
        # Show transitions
        vw = VacuumWorld()
        vw.location, vw.left_dirty, vw.right_dirty = loc, left, right
        actions = vw.get_possible_actions()
        
        for action in actions:
            temp_vw = VacuumWorld()
            temp_vw.location, temp_vw.left_dirty, temp_vw.right_dirty = loc, left, right
            temp_vw.perform_action(action)
            new_state = temp_vw.get_state()
            print(f"  [{action}] → {state_names[new_state]}")


def solve_vacuum_world(start_loc=0, left_dirty=1, right_dirty=1):
    """Simple reflex agent solution"""
    print("\n" + "="*60)
    print("SIMPLE REFLEX AGENT SOLVING VACUUM WORLD")
    print("="*60)
    
    vw = VacuumWorld()
    vw.reset(start_loc, left_dirty, right_dirty)
    
    print(f"\nInitial State: Location={'Left' if start_loc==0 else 'Right'}, "
          f"Left={'Dirty' if left_dirty else 'Clean'}, "
          f"Right={'Dirty' if right_dirty else 'Clean'}\n")
    
    step = 0
    print(f"Step {step}:")
    vw.display()
    
    # Simple reflex agent: if dirty, suck; else move to other room
    while not vw.is_clean() and step < 10:
        step += 1
        
       
        if vw.location == 0:  # In left room
            if vw.left_dirty == 1:
                action = 'S'
            else:
                action = 'R'
        else:  
            if vw.right_dirty == 1:
                action = 'S'
            else:
                action = 'L'
        
        vw.perform_action(action)
        action_name = {'L': 'Move Left', 'R': 'Move Right', 'S': 'Suck'}[action]
        print(f"\nStep {step}: Action = {action_name}")
        vw.display()
    
    print(f"\n{'✓ SUCCESS!' if vw.is_clean() else '✗ FAILED'}")
    print(f"Actions taken: {' → '.join(vw.actions_taken)}")
    print(f"Total steps: {len(vw.actions_taken)}")


def interactive_mode():
    """Interactive vacuum world simulator"""
    print("\n" + "="*60)
    print("INTERACTIVE VACUUM WORLD")
    print("="*60)
    
    vw = VacuumWorld()
    
    print("\nSetup Initial State:")
    loc = input("Starting location (L/R): ").strip().upper()
    vw.location = 0 if loc == 'L' else 1
    
    left = input("Left room dirty? (Y/N): ").strip().upper()
    vw.left_dirty = 1 if left == 'Y' else 0
    
    right = input("Right room dirty? (Y/N): ").strip().upper()
    vw.right_dirty = 1 if right == 'Y' else 0
    
    print("\nInitial State:")
    vw.display()
    
    step = 0
    while True:
        if vw.is_clean():
            print("\n✓ Both rooms are clean! Goal achieved!")
            print(f"Actions: {' → '.join(vw.actions_taken)}")
            break
        
        actions = vw.get_possible_actions()
        print(f"\nPossible actions: {', '.join(actions)}")
        action = input("Enter action (or 'q' to quit): ").strip().upper()
        
        if action == 'Q':
            break
        
        if vw.perform_action(action):
            step += 1
            print(f"\nStep {step}:")
            vw.display()
        else:
            print("Invalid action!")


if __name__ == "__main__":
    generate_state_space()
    
    print("\n" + "="*60)
    solve_vacuum_world(start_loc=0, left_dirty=1, right_dirty=1)
    
    print("\n" + "="*60)
    print("Testing from Right room:")
    solve_vacuum_world(start_loc=1, left_dirty=1, right_dirty=1)
    
    print("\n" + "="*60)
    choice = input("\nTry interactive mode? (y/n): ").strip().lower()
    if choice == 'y':
        interactive_mode()