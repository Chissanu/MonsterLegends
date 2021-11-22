from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("C:\Users\WIndows10\Desktop\School Stuff\KMITL\Intro to Fundamental Programming lang\MonsterLegends\Assets\sound\click.wav")
play(song)

