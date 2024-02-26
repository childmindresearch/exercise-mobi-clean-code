```python
class GREG:
    def __init__(self):
        self.institute = "Child Mind Institute"
        self.research_group = "Group for Research on Emotional Gregs"
        self.techniques = "groundbreaking techniques"
        self.target_audience = "Gregs"
        self.mission = "help Gregs everywhere learn to deal with their complex workplace environments"

    def deliver_innovations(self, team):
        return f"GREG ©, brought to you by {self.institute}, delivers the latest innovations in Greg psychiatry directly to your {team}."

    def help_company(self):
        topics = ["project management", "teambuilding", "c-suite interactions", "raw programming skills"]
        return f"From {' '.join(topics)}, help your company's emotional {self.target_audience} reach their highest potential."

# Example usage:
greg = GREG()
team = "team"
print(greg.deliver_innovations(team))
print(greg.help_company())
```
