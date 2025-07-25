//! A library for calculating the area of various 2D geometric shapes.

// Use PI constant for circle and ellipse calculations.
use std::f64::consts::PI;

/// Calculates the area of a square.
///
/// # Parameters
/// * `s`: The length of a side of the square. All sides are equal.
///
/// # Formula
/// $Area = s^2$
///
/// # Examples
/// ```
/// // Assuming the crate is named 'shapes'
/// let area = shapes::area_square(5.0);
/// assert_eq!(area, 25.0);
/// ```
pub fn area_square(s: f64) -> f64 {
    // Input validation can be added here, e.g., ensure s >= 0.0
    s.powi(2)
}

/// Calculates the area of a rectangle.
///
/// # Parameters
/// * `b`: The length of the base.
/// * `h`: The height.
///
/// # Formula
/// $Area = b \times h$
///
/// # Examples
/// ```
/// let area = shapes::area_rectangle(4.0, 5.0);
/// assert_eq!(area, 20.0);
/// ```
pub fn area_rectangle(b: f64, h: f64) -> f64 {
    b * h
}

/// Calculates the area of a parallelogram.
///
/// # Parameters
/// * `b`: The length of the base.
/// * `h`: The perpendicular height from the base to the opposite side.
///
/// # Formula
/// $Area = b \times h$
///
/// # Examples
/// ```
/// let area = shapes::area_parallelogram(6.0, 4.0);
/// assert_eq!(area, 24.0);
/// ```
pub fn area_parallelogram(b: f64, h: f64) -> f64 {
    b * h
}

/// Calculates the area of a trapezoid.
///
/// # Parameters
/// * `a`: The length of the first parallel side (top base).
/// * `b`: The length of the second parallel side (bottom base).
/// * `h`: The perpendicular height between the parallel sides.
///
/// # Formula
/// $Area = \frac{(a + b)h}{2}$
///
/// # Examples
/// ```
/// let area = shapes::area_trapezoid(5.0, 7.0, 4.0);
/// assert_eq!(area, 24.0);
/// ```
pub fn area_trapezoid(a: f64, b: f64, h: f64) -> f64 {
    (a + b) * h / 2.0
}

/// Calculates the area of a triangle.
///
/// # Parameters
/// * `b`: The length of the base of the triangle.
/// * `h`: The perpendicular height from the base to the opposite vertex.
///
/// # Formula
/// $Area = \frac{1}{2} \times b \times h$
///
/// # Examples
/// ```
/// let area = shapes::area_triangle(10.0, 5.0);
/// assert_eq!(area, 25.0);
/// ```
pub fn area_triangle(b: f64, h: f64) -> f64 {
    0.5 * b * h
}

/// Calculates the area of a circle.
///
/// # Parameters
/// * `r`: The radius of the circle.
///
/// # Formula
/// $Area = \pi r^2$
///
/// # Examples
/// ```
/// let area = shapes::area_circle(10.0);
/// assert!((area - 314.1592653589793).abs() < 1e-9);
/// ```
pub fn area_circle(r: f64) -> f64 {
    PI * r.powi(2)
}

/// Calculates the area of an ellipse.
///
/// # Parameters
/// * `a`: The semi-major axis radius.
/// * `b`: The semi-minor axis radius.
///
/// # Formula
/// $Area = \pi ab$
///
/// # Examples
/// ```
/// let area = shapes::area_ellipse(5.0, 10.0);
/// assert!((area - 157.07963267948966).abs() < 1e-9);
/// ```
pub fn area_ellipse(a: f64, b: f64) -> f64 {
    PI * a * b
}

// The test module.
// This code is only compiled when running `cargo test`.
#[cfg(test)]
mod tests {
    // Import all functions from the parent module (the library itself)
    use super::*;

    const TOLERANCE: f64 = 1e-9;

    #[test]
    fn test_area_square() {
        assert_eq!(area_square(4.0), 16.0);
        assert_eq!(area_square(0.0), 0.0);
        assert!((area_square(1.5) - 2.25).abs() < TOLERANCE);
    }

    #[test]
    fn test_area_rectangle() {
        assert_eq!(area_rectangle(5.0, 4.0), 20.0);
        assert_eq!(area_rectangle(0.0, 10.0), 0.0);
        assert_eq!(area_rectangle(10.0, 0.0), 0.0);
    }

    #[test]
    fn test_area_parallelogram() {
        assert_eq!(area_parallelogram(6.0, 3.0), 18.0);
        assert!((area_parallelogram(2.5, 3.5) - 8.75).abs() < TOLERANCE);
        assert_eq!(area_parallelogram(10.0, 0.0), 0.0);
    }

    #[test]
    fn test_area_trapezoid() {
        assert_eq!(area_trapezoid(3.0, 5.0, 4.0), 16.0);
        // A trapezoid with equal bases is a rectangle
        assert_eq!(area_trapezoid(5.0, 5.0, 2.0), 10.0);
        assert_eq!(area_trapezoid(5.0, 7.0, 0.0), 0.0);
    }

    #[test]
    fn test_area_triangle() {
        assert_eq!(area_triangle(10.0, 4.0), 20.0);
        assert_eq!(area_triangle(7.0, 0.0), 0.0);
        assert!((area_triangle(3.0, 3.0) - 4.5).abs() < TOLERANCE);
    }

    #[test]
    fn test_area_circle() {
        let expected = PI * 5.0 * 5.0;
        assert!((area_circle(5.0) - expected).abs() < TOLERANCE);
        assert_eq!(area_circle(0.0), 0.0);
        assert_eq!(area_circle(1.0), PI);
    }

    #[test]
    fn test_area_ellipse() {
        let expected = PI * 3.0 * 4.0;
        assert!((area_ellipse(3.0, 4.0) - expected).abs() < TOLERANCE);
        // An ellipse with equal radii is a circle
        assert!((area_ellipse(5.0, 5.0) - area_circle(5.0)).abs() < TOLERANCE);
        assert_eq!(area_ellipse(10.0, 0.0), 0.0);
    }
}
