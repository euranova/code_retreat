pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod unit_tests {

    #[test]
    fn add_two() {
      assert_eq!(7, super::add_two(5));
    }
}
