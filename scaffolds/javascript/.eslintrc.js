module.exports = {
  'parserOptions': {
    'ecmaVersion': 7,
    'sourceType': 'module',
    'ecmaFeatures': {
      'modules': true,
    },
  },
  'env': {
    'node': true,
    'mocha': true,
  },
  'extends': ['eslint:recommended'],
  'rules': {
    'no-console': 0,
    'no-unused-vars': 1,
    'comma-dangle': [1, 'only-multiline'],
    'quotes': [1, 'single'],
    'strict': [2, 'never'],
  }
};
