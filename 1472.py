# Design Browser History

class BrowserHistory:

    def __init__(self, homepage: str):
        self.total_steps = 1
        self.current_steps = 1
        self.visited_history = []
        self.current_url = homepage
        self.visited_history.append(homepage)

    def visit(self, url: str) -> None:

        if(self.current_steps == self.total_steps):
            self.visited_history.append(self.current_url)

        else: # current page have visited 
            for i in range(self.total_steps - self.current_steps):
                self.visited_history.pop()
        
        self.current_steps = self.current_steps + 1
        self.total_steps = self.current_steps
        self.current_url = url
        
    def back(self, steps: int) -> str:
        self.current_steps = max(self.current_steps - steps, 1)
        self.current_url = self.visited_history[self.current_steps-1]
        return self.current_url

    def forward(self, steps: int) -> str:
        self.current_steps = min(self.current_steps + steps, self.total_steps)
        self.current_url = self.visited_history[self.current_steps-1]

        return self.current_url
