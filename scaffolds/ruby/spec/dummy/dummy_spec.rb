require_relative '../spec_helper'
require_relative '../../lib/dummy'

# Using minitest, see cheat sheet https://mattsears.com/articles/2011/12/10/minitest-quick-reference/
describe Dummy do
  it "has a dummy constant" do
    expect(Dummy::HELLO).must_equal "Hello Code Retreat!"
  end
end
