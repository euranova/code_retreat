(ns scaffold.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (str x " Hello, World!"))

(defn -main [& args]
  (println (foo "Indeed:")))
