// -----------------------------
// project definition
// -----------------------------

name := "EURA NOVA Code Retreat Scaffold"

version := "0.0.1"

organization := "euranova"

scalaVersion := "2.10.3"

// -----------------------------
// common dependencies
// -----------------------------

libraryDependencies += "org.scalatest" %% "scalatest" % "2.0" % "test"

// -----------------------------
// resolvers (source repositories)
// -----------------------------

resolvers ++= Seq(
  "Typesafe Repository" at "http://repo.typesafe.com/typesafe/releases/",
  "Local Maven Repository" at "file:///"+Path.userHome+"/.m2/repository"
)
