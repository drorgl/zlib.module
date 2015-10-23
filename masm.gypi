#https://github.com/nodejs/node/blob/master/deps/openssl/masm_compile.gypi

{
  'conditions': [
    ['target_arch=="ia32"', {
      'rules': [
        {
          'rule_name': 'Assemble',
		  'msvs_cygwin_shell': 0,
          'extension': 'asm',
          'inputs': [],
          'outputs': [
            '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
          ],
          'action': [
            'ml.exe',
            '/Zi',
            '/safeseh',
            '/Fo', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
            '/c', '<(RULE_INPUT_PATH)',
          ],
          'process_outputs_as_sources': 0,
          'message': 'Assembling <(RULE_INPUT_PATH) to <(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj.',
        }
      ],
    }, 'target_arch=="x64"', {
      'rules': [
        {
          'rule_name': 'Assemble',
		  'msvs_cygwin_shell': 0,
          'extension': 'asm',
          'inputs': [],
          'outputs': [
            '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
          ],
          'action': [
            'ml64.exe',
            '/Zi',
            '/Fo', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
            '/c', '<(RULE_INPUT_PATH)',
          ],
          'process_outputs_as_sources': 0,
          'message': 'Assembling <(RULE_INPUT_PATH) to <(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj.',
        }
      ],
    }],
  ],
}