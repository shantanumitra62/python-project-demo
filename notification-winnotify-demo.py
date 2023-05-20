#import winotify as win

#print(dir(win))

from winotify import Notification, audio

toast = Notification(app_id="Shan's Script", duration="long", title="Hey buddy!!", 
                        msg="Hello Folk you are about to experie magic")

toast.set_audio(audio.LoopingCall, loop=False)

toast.add_actions(label="Click me!", launch="https://google.com", )


toast.show()