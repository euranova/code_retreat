extern crate scaffold;

#[cfg(test)]
mod integration_tests {
    use scaffold::add_two;

    #[test]
    fn it_works() {
        assert_eq!(4, add_two(2));
    }
}
