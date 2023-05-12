#Alarm with only one song to choose and stop button added
import datetime
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.dropdown import DropDown
from kivy.uix.togglebutton import ToggleButton


class TimePicker(FloatLayout):
    def __init__(self, **kwargs):
        super(TimePicker, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        self.hours_input = TextInput(multiline=False, input_filter='int', size_hint=(None, None), size=(40, 40),
                                     pos_hint={'center_x': 0.45, 'center_y': 0.8})
        self.add_widget(self.hours_input)

        self.colon_label = Label(text=':', size_hint=(None, None), size=(50, 50),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.add_widget(self.colon_label)

        self.minutes_input = TextInput(multiline=False, input_filter='int', size_hint=(None, None), size=(40, 40),
                                       pos_hint={'center_x': 0.55, 'center_y': 0.8})
        self.add_widget(self.minutes_input)


class AlarmClock(FloatLayout):
    def __init__(self, **kwargs):
        super(AlarmClock, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.time_picker = TimePicker()
        self.add_widget(self.time_picker)

        self.set_alarm_button = Button(text='Set Alarm', size_hint=(None, None), size=(200, 50),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.65})
        self.set_alarm_button.bind(on_release=self.set_alarm)
        self.add_widget(self.set_alarm_button)

        self.alarm_label = Label(text='')
        self.add_widget(self.alarm_label)

        self.song_dropdown = DropDown()
        self.song_button = Button(text='Select Song', size_hint=(None, None), size=(200, 50),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.song_button.bind(on_release=self.song_dropdown.open)
        self.add_widget(self.song_button)

        self.add_songs()

        self.selected_song = None
        self.alarm_sound = None

        self.stop_alarm_button = Button(text='Stop Alarm', size_hint=(None, None), size=(200, 50),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.stop_alarm_button.bind(on_release=self.stop_alarm)
        self.stop_alarm_button.disabled = True  # Disable the button initially
        self.add_widget(self.stop_alarm_button)

    def add_songs(self):
        songs = [
            "Bloom 04-03-2023 01-21.wav",
            "coconut bar.mp3",
            "Downtempo.wav",
            "elevation.wav",
            "futuristic kitchen no1.mp3",
            "idk.wav",
            "Lo-Fi Lullaby no1.wav",
            "Lo-Fi Lullaby no2.wav",
            "mornin.wav",
            "Ocean View.wav",
            "Sublime DNB.wav",
            "Sunshine Voyage.wav",
            "Welcome at Ellie's.mp3"
        ]

        for song in songs:
            radiobutton = ToggleButton(text=song, size_hint_y=None, height=44, group='songs')
            radiobutton.bind(on_release=self.song_selected)
            self.song_dropdown.add_widget(radiobutton)

    def song_selected(self, button):
        self.selected_song = button.text
        self.load_song()

    def load_song(self):
        if self.selected_song:
            sound_file = self.selected_song
            self.alarm_sound = SoundLoader.load(sound_file)

    def set_alarm(self, *args):
        hours = int(self.time_picker.hours_input.text)
        minutes = int(self.time_picker.minutes_input.text)
        current_datetime = datetime.datetime.now()
        alarm_datetime = current_datetime.replace(hour=hours, minute=minutes, second=0, microsecond=0)

        if alarm_datetime <= current_datetime:
            # If alarm time is earlier or equal to the current time, set it for the next day
            alarm_datetime += datetime.timedelta(days=1)

        time_difference = alarm_datetime - current_datetime
        total_seconds = time_difference.total_seconds()
        self.alarm_label.text = f"Alarm set for {alarm_datetime.strftime('%H:%M')}."

        # Schedule the alarm callback
        Clock.schedule_once(self.alarm_callback, total_seconds)

    def alarm_callback(self, dt):
        self.alarm_label.text = "Wake up!"

        # Play the alarm sound
        if self.alarm_sound:
            self.alarm_sound.play()

        self.stop_alarm_button.disabled = False  # Enable the stop alarm button

    def stop_alarm(self, *args):
        self.alarm_label.text = ""  # Clear the alarm label

        # Stop the alarm sound
        if self.alarm_sound:
            self.alarm_sound.stop()

        self.stop_alarm_button.disabled = True  # Disable the stop alarm button


class AlarmClockApp(App):
    def build(self):
        return AlarmClock()


if __name__ == '__main__':
    AlarmClockApp().run()

