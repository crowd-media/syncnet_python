import os
import sys

## add current dir to sys path so that root method py files can be imported from outside 
current_dir = os.path.dirname( __file__ )
sys.path.append( current_dir )