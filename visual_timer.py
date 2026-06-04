import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib, Gdk
import math
import time

# --- Настройки внешнего вида ---
SIZE_PX = 75            # ~2 см диаметр
LINE_WIDTH = 6
COLOR_BG = (0.3, 0.3, 0.3, 0.4)   # Серый фон круга
COLOR_FG = (0.2, 0.8, 0.4, 1.0)   # Зеленый прогресс

# --- Обязательный аргумент времени ---
if len(sys.argv) != 2:
    print("Ошибка: укажите время в минутах")
    print("Пример: python3 visual_timer.py 45")
    sys.exit(1)

try:
    minutes = int(sys.argv[1])
    if minutes <= 0:
        raise ValueError
except ValueError:
    print("Ошибка: время должно быть положительным целым числом")
    sys.exit(1)

DURATION_SEC = minutes * 60


class VisualTimer(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.custom.visualtimer")
        self.start_time = None
        self.active = False
        self.timeout_id = None

    def do_activate(self):
        win = Gtk.ApplicationWindow(application=self, title="Visual Timer")
        win.set_default_size(SIZE_PX, SIZE_PX)
        win.set_decorated(False)
        win.set_resizable(False)
        win.set_keep_above(True)
        win.set_overflow(Gtk.Overflow.HIDDEN)


        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.set_content_width(SIZE_PX)
        self.drawing_area.set_content_height(SIZE_PX)
        self.drawing_area.set_draw_func(self.draw_circle)
        win.set_child(self.drawing_area)

        click = Gtk.GestureClick.new()
        click.connect("pressed", self.on_click)
        self.drawing_area.add_controller(click)

        win.present()

    def on_click(self, gesture, n_press, x, y):
        if self.active:
            self.stop()
        else:
            self.start()

    def start(self):
        self.active = True
        self.start_time = time.time()
        self.timeout_id = GLib.timeout_add(100, self.tick)

    def stop(self):
        self.active = False
        if self.timeout_id:
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
        self.drawing_area.queue_draw()

    def tick(self):
        elapsed = time.time() - self.start_time
        progress = max(0, 1.0 - elapsed / DURATION_SEC)
        self.drawing_area.queue_draw()
        if progress <= 0:
            self.stop()
            return False
        return True

    def draw_circle(self, area, cr, width, height):
        cx, cy = width / 2, height / 2
        radius = min(width, height) / 2 - LINE_WIDTH

        cr.set_source_rgba(*COLOR_BG)
        cr.set_line_width(LINE_WIDTH)
        cr.arc(cx, cy, radius, 0, 2 * math.pi)
        cr.stroke()

        if self.active and self.start_time:
            elapsed = time.time() - self.start_time
            progress = max(0, 1.0 - elapsed / DURATION_SEC)
            if progress > 0:
                cr.set_source_rgba(*COLOR_FG)
                cr.set_line_width(LINE_WIDTH)
                start_angle = -math.pi / 2
                end_angle = start_angle + 2 * math.pi * progress
                cr.arc(cx, cy, radius, start_angle, end_angle)
                cr.stroke()


app = VisualTimer()
app.run(None)
