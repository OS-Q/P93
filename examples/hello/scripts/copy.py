Import("env")
import shutil
import os
#
# Dump build environment (for debug)
# print env.Dump()
#

#
# Upload actions
#


exe_source = os.path.join(env.subst("$BUILD_DIR"), "program.exe")
if os.path.exists(exe_source):
	shutil.copy(exe_source, 'exe')

def after_build(source, target, env):
	shutil.copy(exe_source, 'exe')

env.AddPostAction("buildprog", after_build)

# exe_source = os.path.join(env.subst("$BUILD_DIR"), "program.exe")
# print(exe_source)