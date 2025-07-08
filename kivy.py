from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.clock import Clock

class BallWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1)
            self.ball = Ellipse(pos=(0, 0), size=(50, 50))
        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    def update(self, dt):
        x, y = self.ball.pos
        x += 5
        y += 5
        self.ball.pos = (x, y)

class MyApp(App):
    def build(self):
        return BallWidget()

if __name__ == '__main__':
    MyApp().run()
