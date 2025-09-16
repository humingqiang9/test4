import Foundation

/// A structure representing a point in 2D space
struct Point {
    /// The x-coordinate of the point
    var x: Double
    
    /// The y-coordinate of the point
    var y: Double
    
    /// Initializes a new point with the specified coordinates
    /// - Parameters:
    ///   - x: The x-coordinate
    ///   - y: The y-coordinate
    init(x: Double, y: Double) {
        self.x = x
        self.y = y
    }
    
    /// Calculates the distance from this point to another point
    /// - Parameter other: The other point
    /// - Returns: The distance between the two points
    func distance(to other: Point) -> Double {
        let deltaX = x - other.x
        let deltaY = y - other.y
        return sqrt(deltaX * deltaX + deltaY * deltaY)
    }
}