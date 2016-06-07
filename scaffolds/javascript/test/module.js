const should = require('should');

const Module = require('../src/module');

describe('Module', function(){
  describe('dummy method', function(){
    it('should return a lowercased string passed to it', function(){
      (new Module()).dummy('TEST').should.equal('test');
    })
  });
});
