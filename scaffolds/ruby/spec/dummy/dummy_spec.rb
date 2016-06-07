require "spec_helper"
require "dummy"

describe Dummy do
  it "has a dummy constant" do
    expect(Dummy::HELLO).must_equal "Hello Code Retreat!"
  end
end
