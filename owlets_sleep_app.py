import kivy
import os
import random
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

from kivy.uix.popup import Popup
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = (450, 780)


class HomePage(Screen):  # App home screen.
    pass

# Age group class
class Q1(Screen):   #Question 1.

    num=5  # variable outside the main function to pass name later.

    # function that takes user's age group choice and also each group's number id.
    # group a=0, b=2, c=3 e.t.c.

    def pressbtn(self,age,age1,age2,age3,age4,age5):

        a=f'{age} '  # Need this variable to pass the age group to class Q3.
        #print(a)

        # We use a list( ages_arr ), where each age group is stored separately.

        ages_arr = [0]*5
        ages_arr[0] = f'{age1} '
        ages_arr[1] = f'{age2} '
        ages_arr[2] = f'{age3} '
        ages_arr[3] = f'{age4} '
        ages_arr[4] = f'{age5} '

        # for loop to check if parameter 'age' matches any of the previous lists components.
        for i in range(5):
            if a==ages_arr[i]:
                self.num=i
        #print(self.num)

        # Inner function to pass age group to  class Q4
        def __str__():
            a=self.num
            return a

        __str__()
        Q1.pressbtn.__str__= __str__
    pressbtn.__str__=int(num)


# Hours of sleep per night class
class Q3(Screen):  # Question 3.

        total_h=0    # variable outside the main function to pass name later.

        # function that takes total hours of sleep per night and returns the total hours of sleep per week.
        def q33(self, total):

            #print(f'total hours:{total}')
            per_night = f'{total}'

            self.total_h = 7 * int(per_night)  # multiplies 'per_night' by 7 to estimate weekly hours of sleep.
            #print(self.total_h)

            def total_sleep():  # Inner function to pass hours of sleep to class Q4.
                h=self.total_h
                return self.total_h

            total_sleep()
            Q3.q33.total_sleep=total_sleep
        q33.total_sleep=int(total_h)


# Username class
class Q4(Screen):

    name='0'

    # function to enter username
    def register(self):

        self.name=self.ids.user_input.text
        #print("Username: ",self.ids.user_input.text)

        def pass_name():
            a=self.name
            return (self.name)

        pass_name()
        Q4.register.pass_name=pass_name
    register.pass_name=(name)


# Commentary class
class Comments(Screen): # End of quiz and comments.

    def com(self):

        age =Q1.pressbtn.__str__() #

        hours = int(Q3.q33.total_sleep())

        b=str(hours) # turn int to str to use later in the comments.

        #FIRST COMMENT:

        self.ids.sleep.text=f'Total hours of sleep per week: {b} '


        # SECOND COMMENT:

        if ((age == 0)and(hours < (7 * 11)))or((age == 1)and(hours < 7 * 10))or(
                (age == 2)and(hours < (7 * 9) - 1))or((age == 3)and(hours < (7 * 8) - 5))or(
                (age == 4)and(hours < 7 * 7)):

            self.ids.extra.text = '      Your total falls under\nthe healthy amount of sleep'

        #SPECIAL COMMENTS FOR AGE GROUP 18+:

        elif(age!=4):
            self.ids.extra.text ='The amount of sleep you are getting\n            is considered healthy!\n                      Good job!\n'

        if((age==4) and (hours >= ((9*7)-3))):

            self.ids.extra.text = '       The amount of sleep you are \n  getting is considered healthy! With \n  this hours of sleep at your age you\n have definately cracked the system\n'

        elif((age==4) and (hours >=((7*7)-2))):

            self.ids.extra.text ='The amount of sleep you are getting\n            is considered healthy!\n                      Good job!\n           Honestly, it\'s a miracle\n        you even sleep this much...\n'

        elif((age==4) and (hours <= 6*7)):
            self.ids.extra.text ='        Your total falls under\n   the healthy amount of sleep...\n         Can\'t really blame you\n      in this economy but still...\n     you need to get it together\n       if you want to function \n    like a normal human being'


# class for default sleep schedule display and modification.
class Default(Screen):  # For schedule creation


    # create dictionary with basic time periods to update later and display them directly on you screen

    btn_labels_store = [('00:00-00:00'), ('10:00-00:00'), ('20:00-00:00'), ('30:00-00:00'), ('40:00-00:00'), ('50:00-00:00'), ('60:00-00:00'), ('70:00-00:00'),
                        ('80:00-00:00'), ('90:00-00:00'), ('10:00-00:00'), ('11:00-00:00'), ('12:00-00:00'), ('13:00-00:00')]

    time_f='0'

    # function to create a default sleep schedule based on your age group.
    def btn_labels_age_based(self):

        ag = int(Q1.pressbtn.__str__()) # ag= the age variable given from class Q1.
        #print(ag)

        if ag==0:
            for i in range(7):
                self.ids[str(i)].text='19:30 - 06:30'  # sleep-time
                self.ids[str(i+7)].text = '14:00 - 15:00'   # nap-time

        elif ag==1:
            for i in range(7):
                self.ids[str(i)].text='19:30 - 06:30'
                self.ids[str(i+7)].text = '14:00 - 15:00'

        elif ag==2:
            for i in range(7):
                self.ids[str(i)].text='21:00 - 07:00'
                self.ids[str(i+7)].text = '-'

        elif ag==3:
            for i in range(7):
                self.ids[str(i)].text='22:00 - 07:00'
                self.ids[str(i+7)].text = '-'

        elif ag==4:
            for i in range(7):
                self.ids[str(i)].text='23:00 - 07:30'
                self.ids[str(i+7)].text = '-'

    class ConfirmPopup(Popup):  # Time selection
        q2=''
        q=''
        f_s = ''
        final = 'a'
        final2='b'


        # Get time (TIME SELECTION START)
        # it takes the time given from the time picker.

        def get_time(self, instance,time):

            self.ids.start.text = str(time)
            #print(str(time))
            start = str(time)  # start of sleep.

            st = [0] * 5 # list for label update .1

            for i in range(5):

                st[i] = start[i]
                self.final+= start[i]
            self.final=st
            self.final.append("-") # when everything is settled in, add '-'.

            # final result: e.g. 12:00:00 --> 12:00 --> 12:00-


        # Cancel
        def on_cancel(self,instance,time):
            self.ids.start.text ='Enter time'


        # Get time2 (TIME SELECTION FINISH)
        # it takes the time given from the time picker.

        def get_time2(self, instance,time):

            self.ids.finish.text = str(time)

            #print(str(time))
            finish=str(time)  # end of sleep

            fin=[0]*5     # list for label update 2 (combine later with update 1).

            for i in range(5):
                fin[i] = finish[i]
            self.final2=fin

            # final result: e.g. 13:00:00 --> 13:00

            # Inner function to change button's text in class Default
            def time_array():
                time_label1= self.final
                time_label2 = self.final2

                self.q=str(self.final)+str(self.final2)  # combine start and end of sleep in one variable.

                print(self.q)
                return self.q
            time_array()
            Default.ConfirmPopup.get_time2.time_array=time_array
        get_time2.time_array=str(q)


        # Cancel2
        def on_cancel2(self,instance,time):

            # if the user chooses 'cancel' instead of 'ok' the following message appears:
            self.ids.finish.text ='Enter time'


        # Function for time picker
        def show_time_picker2(self):


            from datetime import datetime

            # default time when accessing time picker for night-time .
            default_time2=datetime.strptime("6:00:00",'%H:%M:%S').time()

            # default time when accessing time picker for nap-time .
            default_time1 = datetime.strptime("1:00:00", '%H:%M:%S').time()


            # time picker for end of sleep:

            time_dialog2 = MDTimePicker()
            time_dialog2.set_time(default_time2)
            time_dialog2.bind(on_cancel=self.on_cancel2, time=self.get_time2)
            time_dialog2.open()

            # time picker for start of sleep:

            time_dialog = MDTimePicker()
            time_dialog.set_time(default_time1)
            time_dialog.bind(on_cancel=self.on_cancel,time=self.get_time)
            time_dialog.open()

    f='0'

    # function to set timer so the user has time to update the time when pressing any button
    # in the default schedule.

    # the function takes the id of the pressed button.
    def pass_label_from_popup(self,id):

        Clock.schedule_once(self.change_text,30)  # Go to function change_text and start a timer of 30 seconds.

        # nested function to pass the id.
        def num():
            self.f=f'{id}'
            f2=self.f
            return f2
        num()
        Default.pass_label_from_popup.num=num
    pass_label_from_popup.num=str(f)

    # the function activated when the mark of 30 sec. if finished.
    def change_text(self,dt):

        f2=Default.pass_label_from_popup.num()  # f2= id from f. 'num'.

        for i in range(14):

            # if the numer of the id matches i, then go to the correct button and update the text.
            if i==int(f2):

                # q= the time picked from the user in class Default.
                q=str(Default.ConfirmPopup.get_time2.time_array())

                # empty the previous text
                label=''


                for j in range(55):

                    # if a variable of the list q qualifies, add it in the label to create the final text.
                    if(q[j]!='[')and(q[j]!=']')and(q[j]!="'")and(q[j]!=',')and(q[j]!=' '):
                        label+=q[j]

                #print(label)

                self.ids[str(i)].text= label
                self.btn_labels_store[i]=label

                #print(self.btn_labels_store[0])

    def update_schedule(self):

        # update the dictionary for future use in the profile menu.
        for i in range(14):
            self.btn_labels_store[i]=self.ids[str(i)].text



    def sighn_label(self):

        label=''

        label += ''
        label+= f'                                                                                            USER: {Q4.register.pass_name()}\n\n'

        # NIGHT TIME PART OF SCHEDULE:
        label += '                                                                                        NIGHT-TIME:\n\n'
        label += '            SUN                    MON                  TUE                      WED                   THUR                   FRI                      SAT  \n\n'

        for i in range(7):
            label += f'    {Default.btn_labels_store[i]}'  # match hours of sleep under each day.

        label += '\n\n\n'
        label += '                                                                                         NAP-TIME:\n\n'
        label += '            SUN                    MON                  TUE                      WED                   THUR                   FRI                      SAT  \n\n'

        # NAP TIME PART OF SCHEDULE:
        for i in range(7):

            if Default.btn_labels_store[i + 7] == '-' and i > 2:

                label+= f'                  {Default.btn_labels_store[i + 7]}          '

            elif Default.btn_labels_store[i + 7] != '-':

                label+= f'   {Default.btn_labels_store[i + 7]}'

            else:

                label += f'                {Default.btn_labels_store[i + 7]}           '

        print(label)
        return (label)


    #def assingh_to_file(self):
        #if( os.path.getsize('profile_1.txt') == 0 ):
           # fob = open('profile_1.txt.', 'w')
           # write = fob.write(str(Default.sighn_label()))


class Main_menu(Screen):

    # Extra's button in menu class.
    class ConfirmPopup2(Popup):


        # class for buss stations in Corfu

        class ConfirmPopup_bus(Popup):

            pass

        # class for articles related to sleep

        class Real_articles(Popup):
            pass

    # Popup class to update profile schedule.
    class ConfirmPopup4(Popup):

        # function to show the updated sleep schedule
        # it takes the id of the button pressed.

        def show_schedule(self,id):

            j_label=f'{id}'# 0
            b=1 #1 name of file

            a=int(j_label)+10 # adds 10 to the original id to match the label bound to it. If button id is 0, then label id is 10
            j=str(a) # turn int to str to be able to access the label's id
                     #10

            # we use for in case multiple profiles are added.
            if(self.ids[j].text=='000'): # check if the label text is correct and then proceed to update it.

                self.ids[j].text =''
                self.ids[j].text =f'                                                                                            USER: {Q4.register.pass_name()}\n\n'

                # NIGHT TIME PART OF SCHEDULE:
                self.ids[j].text +='                                                                                        NIGHT-TIME:\n\n'
                self.ids[j].text +='            SUN                    MON                  TUE                      WED                   THUR                   FRI                      SAT  \n\n'

                for i in range(7):

                    self.ids[j].text+=f'    {Default.btn_labels_store[i]}'  # match hours of sleep under each day.

                self.ids[j].text +='\n\n\n'
                self.ids[j].text +='                                                                                         NAP-TIME:\n\n'
                self.ids[j].text +='            SUN                    MON                  TUE                      WED                   THUR                   FRI                      SAT  \n\n'

                # NAP TIME PART OF SCHEDULE:
                # This row also takes extra parameters in case the user did not pick nap time hours.

                for i in range(7):


                    if Default.btn_labels_store[i+7]=='-'and i>2:

                        self.ids[j].text += f'                  {Default.btn_labels_store[i + 7]}          '

                    elif Default.btn_labels_store[i+7]!='-':

                        self.ids[j].text+=f'   {Default.btn_labels_store[i+7]  }'

                    else:

                        self.ids[j].text += f'                {Default.btn_labels_store[i + 7]}           '


        # function to delete the profile
        # it takes the buttons id and binds the correct label to it like the previous function.

        def delete_schedule(self,id):

            # same as the function before.
            j_label = f'{id}'
            a = int(j_label) + 10
            j = str(a)

            #self.ids[j].size_hint = (1, 0.2)
            self.ids[j].text='Emty spot'        # update label text.


# class for randomized tips
class Random_Tips(Screen):


    tips=[("Make sure your bedroom is\nquiet, dark, relaxing, and at a comfortable temperature."),
          ("Avoid large meals, caffeine,\nand alcohol before bedtime."),
          ('Get some exercise.\nBeing physically active during the day can help you\n fall asleep more easily at night.'),
          ('Limit daytime naps:\nLong daytime naps can interfere with nighttime sleep.'),
          ('Limit naps to no more than\none hour and avoid napping late in the day.'),
          ('If you often have trouble sleeping,\ncontact your health care provider.'),
          ('Do not clock watch:\nWorrying about getting enough sleep\ncan itself stop us sleeping.'),
          ('For many, drinking coffee or other\ncaffeinated drinks in the afternoon can affect sleep.'),
          ('It’s best to avoid having\ntoo many liquids before going to bed.'),
          ('A darkened room helps to promote sleep\nand turning the lights down can make you feel sleepy. '),
          ('For many, drinking coffee or other\ncaffeinated drinks in the afternoon can affect sleep.'),
          ('Know when to contact your health care provider:\nNearly everyone has an occasional sleepless night.'),
          ('Identifying and treating any underlying causes can help you get the better sleep you deserve.'),
          ('Get into a routine:\nWe all know that having a routine helps babies\nand children fall asleep at a certain time.'),
          ('Getting into a routine allows your body\nto programme itself to naturally fall asleep\n and wake up at certain times.'),
          ('Try to be rigid about going to bed at a certain time,\nand create your own relaxation routine.'),
          ('If you cannot stop checking your clock,\ntry turning it around or putting it on the other side\nof the room so it is not as easy to watch time ticking away.'),
          ('Foods for sleeping:\nEating healthily improves sleep generally,\nbut some foods are particularly beneficial, such as\nmilk, chicken, turkey and pumpkin seeds. '),
          ('Milk, chicken, turkey and pumpkin seeds\ncontain the chemicals tryptophan and serotonin,\nwhich are vital for the production of melatonin,\nthe hormone that promotes sleep.'),
          ('Foods to avoid:\nCoffeeSpicy food, alcohol and large meals\nshould not be consumed in the hours before bedtime.'),
          ('Sugary food in general is bad,\nbecause the energy spike and ensuing crash\nyou get can play havoc with your body clock.'),
          ('Research has shown that,\nif you do not sleep well,\nyou tend to turn to junk food the next day,\ncreating a vicious cycle of poor sleep and bad diet.'),
          ('Darkness promotes sleep:\nBefore clocks, people would wake up when\nthe sun rose and go to sleep when it got dark.'),
          ('If you do not have a dimmer switch,\ninexpensive lamps with a dimmer are a good option,\n or you could ask an electrician to quote\n for the cost of changing your main light switch.'),
          ('If you are disturbed by street lights outside your window,\nor bright sunlight at 5am in summer,\nyou could try heavier curtains, extra lining\nor investing in blackout blinds.'),
          ]

    def tip_of_the_day(self):

        random_election = random.randint(0,25)
        self.ids.tip.text=self.tips[random_election]


# class to connect all 'Screen' classes in the kivy.kv file.
class ScreenManagement(ScreenManager):
    pass


class StartApp(MDApp):  # main function.

    def build(self):
        return Builder.load_file("kivy.kv");   # Returns kivy.kv functions and widgets, screen attributes e.t.c.

StartApp().run()
