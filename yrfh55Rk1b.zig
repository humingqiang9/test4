// Point structure in Zig
// File name: yrfh55Rk1b.zig

const std = @import("std");

// Structure to represent a point in 2D space
pub const Point = struct {
    x: f64,
    y: f64,
    
    // Initialize a new point
    pub fn init(x: f64, y: f64) Point {
        return Point{ .x = x, .y = y };
    }
    
    // Calculate distance from origin
    pub fn distanceFromOrigin(self: Point) f64 {
        return std.math.sqrt(self.x * self.x + self.y * self.y);
    }
    
    // Calculate distance to another point
    pub fn distanceTo(self: Point, other: Point) f64 {
        const dx = self.x - other.x;
        const dy = self.y - other.y;
        return std.math.sqrt(dx * dx + dy * dy);
    }
    
    // Move point by dx, dy
    pub fn translate(self: *Point, dx: f64, dy: f64) void {
        self.x += dx;
        self.y += dy;
    }
};

// Example usage
pub fn main() void {
    var point1 = Point.init(3.0, 4.0);
    var point2 = Point.init(0.0, 0.0);
    
    std.debug.print("Point 1: ({d}, {d})\n", .{ point1.x, point1.y });
    std.debug.print("Distance from origin: {d}\n", .{point1.distanceFromOrigin()});
    
    std.debug.print("Point 2: ({d}, {d})\n", .{ point2.x, point2.y });
    std.debug.print("Distance between points: {d}\n", .{point1.distanceTo(point2)});
    
    point1.translate(1.0, 1.0);
    std.debug.print("Point 1 after translation: ({d}, {d})\n", .{ point1.x, point1.y });
}