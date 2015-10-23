{
	'variables':{
		#'library' : 'static_library',
		'library' : 'shared_library',
	},

	'target_defaults': {
		'configurations':{
			'Debug':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'defines':[
					'DEBUG',
				],
				'msvs_settings': {				
					'VCLinkerTool' : {
						'GenerateDebugInformation' : 'true',
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
			'Release':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'msvs_settings': {				
					'VCLinkerTool' : {
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
		},
		
		'msvs_settings': {
			'VCCLCompilerTool':{
				'Optimization':'3',#'MaxSpeed'
				'OmitFramePointers': 'true',
			},
		},
		
		'conditions':[
			
			['OS == "win"',{
				'includes': ['masm.gypi'],
			}],
			
			['OS=="linux" and target_arch=="ia32"',{
				'cflags':[
					'-m32',
				],
				'ldflags':[
					'-m32',
					'-L/usr/lib32',
					'-L/usr/lib32/debug',
				],
			}],
			['OS=="linux" and target_arch=="x64"',{
				'cflags':[
					'-m64'
				],
				'ldflags':[
					'-m64',
				],
			}],
		],
	},
	
	'targets':
	[
		{
			'target_name': 'zlib',
			'type':'<(library)',
			
			'include_dirs':[
				'.',
				'include',
				'zlib_src'
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'.',
					'include',
					'zlib_src'
				],
				'conditions':[
					['OS == "win" and library == "shared_library"',{
						'defines':[
							#'ZLIB_DLL',
							
						],
					}],
				]
			 },
			'sources':[
				'zlib_src/adler32.c',
				'zlib_src/compress.c',
				'zlib_src/crc32.c',
				'zlib_src/crc32.h',
				'zlib_src/deflate.c',
				'zlib_src/deflate.h',
				'zlib_src/gzclose.c',
				'zlib_src/gzguts.h',
				'zlib_src/gzlib.c',
				'zlib_src/gzread.c',
				'zlib_src/gzwrite.c',
				'zlib_src/infback.c',
				'zlib_src/inffast.c',
				'zlib_src/inffast.h',
				'zlib_src/inffixed.h',
				'zlib_src/inflate.c',
				'zlib_src/inflate.h',
				'zlib_src/inftrees.c',
				'zlib_src/inftrees.h',
				'zlib_src/trees.c',
				'zlib_src/trees.h',
				'zlib_src/uncompr.c',
				'zlib_src/zlib.h',
				'zlib_src/zutil.c',
				'zlib_src/zutil.h',			
			],
			'conditions':[
				['OS in "android linux"',{
					'defines':[
						'NO_UNDERLINE',
					],
					
					'conditions':[
						['library == "static_library" and target_arch in "x64"',{
							'sources':[
								'zlib_src/contrib/inflate86/inffas86.c',
							],
						}],
						['target_arch=="x64" and library == "static_library"', {
							'defines':[
								'ASMV',
								'ASMINF',
							],
							'sources':[
								#'zlib_src/contrib/amd64/amd64-match.S',
								'zlib_src/contrib/gcc_gvmat64/gvmat64.S',
							],
						}],
						['library == "shared_library"',{
							'cflags':[
								'-fPIC',
							],
							
						}],
					]
					
				}],
				['OS == "win"',{
					'defines':[
						'_CRT_SECURE_NO_DEPRECATE',
						'_CRT_NONSTDC_NO_DEPRECATE',
						'ASMV',
						'ASMINF',
					],
					
					'conditions':[
						['target_arch=="x64"', {
							'sources':[
								'zlib_src/contrib/masmx64/gvmat64.asm',
								'zlib_src/contrib/masmx64/inffas8664.c',
								'zlib_src/contrib/masmx64/inffasx64.asm',
							],
						}],
						['target_arch=="ia32"',{
							'sources':[
								'zlib_src/contrib/masmx86/inffas32.asm',
								'zlib_src/contrib/masmx86/match686.asm',
							],
						}],
					]
				}],
				['OS == "win" and library == "shared_library"',{
					'defines':[
						#'ZLIB_DLL',
						#'ZLIB_INTERNAL',
					],
					'sources':[
						'zlib_src/win32/zlib1.rc',
						'zlib_src/win32/zlib.def',
					],
					
					
					
				}],
			]
		},
		{
			'target_name':'minigzip',
			'type':'<(library)',
			
			'dependencies':[
				'zlib',
			],
			
			'include_dirs':[
				'.',
				'zlib_src',
				'zlib_src/contrib/minizip',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'.',
					'zlib_src'
					'zlib_src/contrib/minizip',
				],
				'conditions':[
					['OS == "win" and library == "shared_library"',{
						'defines':[
							'ZLIB_DLL',
						],
					}],
					
				]
			 },
			 
			 'sources':[
				'zlib_src/contrib/minizip/crypt.h',
				'zlib_src/contrib/minizip/ioapi.c',
				'zlib_src/contrib/minizip/ioapi.h',
				'zlib_src/contrib/minizip/MiniZip64_Changes.txt',
				'zlib_src/contrib/minizip/MiniZip64_info.txt',
				'zlib_src/contrib/minizip/mztools.c',
				'zlib_src/contrib/minizip/mztools.h',
				'zlib_src/contrib/minizip/unzip.c',
				'zlib_src/contrib/minizip/unzip.h',
				'zlib_src/contrib/minizip/zip.c',
				'zlib_src/contrib/minizip/zip.h',			
			 ],
			 
			 'conditions':[
				['OS == "win"',{
					'sources':[
						'zlib_src/contrib/minizip/iowin32.c',
						'zlib_src/contrib/minizip/iowin32.h',
					],
				}],
				['OS in "linux android" and library == "shared_library"',{
					'cflags':[
						'-fPIC',
					],
				}],
			 ],
		},
		
		{
			'target_name': 'example',
			'type':'executable',
			
			'dependencies':[
				'zlib',
			],
			
			'sources':[
				'zlib_src/test/example.c',
			],
		
		},
		{
			'target_name': 'minigzip_',
			'type':'executable',
			
			'dependencies':[
				'zlib',
			],
			
			'sources':[
				'zlib_src/test/minigzip.c',
			],
		
		}
		
		
	],
	
	'conditions':[
		['OS == "win"',{
			'targets':[
				{
					'target_name': 'testzlib',
					'type':'executable',
					'dependencies':[
						'zlib',
					],
					
					'sources':[
						'zlib_src/contrib/testzlib/testzlib.c',
					],
				
				},				
			]
		}],
	]
}