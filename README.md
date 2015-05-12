# zlib GYP Module

** Experimental **

expose zlib through gyp

- can be used stand alone to compile zlib as static/shared libraries ( / dll) and zlib example
	static/shared library can be changed in the variables section of zlib.gyp
- can be used as part of a bigger gyp project (which was the original intent) :
'dependencies':[
	'zlib.module/zlib.gyp:zlib'
]

zlib source https://github.com/madler/zlib

gyp zlib.gyp -DOS=win -Dtarget_arch=ia32 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/
gyp zlib.gyp -DOS=win -Dtarget_arch=x64 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp zlib.gyp -DOS=linux -Dtarget_arch=ia32 --depth=. -f make --generator-output=./build.linux32/
gyp zlib.gyp -DOS=linux -Dtarget_arch=x64 --depth=. -f make --generator-output=./build.linux64/

gyp zlib.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/

