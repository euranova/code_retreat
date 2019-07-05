import { random } from "../src/module";

describe("random", () => {
    it("gives a random number between 1 and 6", () => {
        expect(random()).toBe(4);
    });
});
