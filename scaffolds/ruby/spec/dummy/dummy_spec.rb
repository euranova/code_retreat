require_relative '../spec_helper'
require_relative '../../lib/dummy'

describe Dummy do
  it "has a dummy constant" do
    expect(Dummy::HELLO).must_equal "Hello Code Retreat!"
  end
end
