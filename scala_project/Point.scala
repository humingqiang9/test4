// Point.scala
// This file defines a case class to represent a point in 2D space.

/** A case class representing a point in 2D space.
  *
  * @param x The x-coordinate of the point.
  * @param y The y-coordinate of the point.
  */
case class Point(x: Double, y: Double)

// Companion object can be used for additional utilities or implicit conversions if needed.
object Point {
  // Example of a utility method to calculate the distance from the origin.
  def distanceFromOrigin(p: Point): Double = math.sqrt(p.x * p.x + p.y * p.y)
}