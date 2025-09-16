const std = @import("std");

// Point structure in Zig
// This structure stores information about a point in 2D space

const Point = struct {
    x: f32,
    y: f32,
    
    // Method to initialize a new point
    pub fn init(x: f32, y: f32) Point {
        return Point{ .x = x, .y = y };
    }
    
    // Method to calculate distance from origin
    pub fn distanceFromOrigin(self: Point) f32 {
        return std.math.sqrt(self.x * self.x + self.y * self.y);
    }
    
    // Method to display point information
    pub fn display(self: Point) void {
        std.debug.print("Point({d:.2}, {d:.2})\n", .{self.x, self.y});
    }
};

// Example usage
pub fn main() void {
    const p1 = Point.init(3.0, 4.0);
    p1.display();
    std.debug.print("Distance from origin: {d:.2}\n", .{p1.distanceFromOrigin()});
}