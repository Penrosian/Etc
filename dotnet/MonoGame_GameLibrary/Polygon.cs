using System;
using System.Linq;
using Microsoft.Xna.Framework;

namespace MonoGame_GameLibrary;

/// <summary>
/// Creates a new polygon with the specified vertices.
/// </summary>
/// <param name="points">The points that make up the polygon.</param>
public readonly struct Polygon(Point[] points) : IEquatable<Polygon>
{
    private static readonly Polygon p_empty = new();

    /// <summary>
    /// The points that make up the polygon.
    /// </summary>
    public readonly Point[] Vertices = points;

    /// <summary>
    /// Gets a polygon with X=0, Y=0, and Radius=0.
    /// </summary>
    public static Polygon Empty => p_empty;

    /// <summary>
    /// Gets a value that indicates whether this polygon has no vertices.
    /// </summary>
    public readonly bool IsEmpty => Vertices.Length == 0;

    private Vector2[] getEdges()
    {
        Vector2[] edges = new Vector2[Vertices.Length];
        for (int i = 0; i < Vertices.Length; i++)
        {
            if (i == Vertices.Length - 1)
            {
                edges[i] = new Vector2(Vertices[0].X - Vertices[i].X, Vertices[0].Y - Vertices[i].Y);
            }
            else
            {
                edges[i] = new Vector2(Vertices[i+1].X - Vertices[i].X, Vertices[i+1].Y - Vertices[i].Y);
            }
        }
        return edges;
    }

    /// <summary>
    /// Returns a value that indicates whether the specified rectangle intersects with this polygon.
    /// </summary>
    /// <param name="rectangle">The other rectangle to check.</param>
    /// <returns>true if the other rectangle intersects with this polygon; otherwise, false.</returns>
    public bool Intersects(Rectangle rectangle)
    {
        Polygon rectPoly = new Polygon(new Point[]
        {
            new Point(rectangle.Left, rectangle.Top),
            new Point(rectangle.Right, rectangle.Top),
            new Point(rectangle.Right, rectangle.Bottom),
            new Point(rectangle.Left, rectangle.Bottom)
        });
        return Intersects(rectPoly);
    }

    /// <summary>
    /// Returns a value that indicates whether the specified polygon intersects with this polygon.
    /// </summary>
    /// <param name="other">The other polygon to check.</param>
    /// <returns>true if the other polygon intersects with this polygon; otherwise, false.</returns>
    public bool Intersects(Polygon other)
    {
        // https://www.youtube.com/watch?v=MvlhMEE9zuc
        int dot = 0;
        Vector2[] perpindicularStack = [];
        int? amin;
        int? amax;
        int? bmin;
        int? bmax;
        Vector2[] Edges = getEdges();
        Vector2[] otherEdges = other.getEdges();
        for (int i = 0; i < Edges.Length; i++)
        {
            perpindicularStack[i] = new Vector2(-Edges[i].Y, Edges[i].X);
        }
        for (int i = 0; i < otherEdges.Length; i++)
        {
            perpindicularStack[i] = new Vector2(-otherEdges[i].Y, otherEdges[i].X);
        }
        for (int i = 0; i < perpindicularStack.Length; i++)
        {
            amin = null;
            amax = null;
            bmin = null;
            bmax = null;
            for (int j = 0; j < Vertices.Length; j++)
            {
                dot = (int)(Vertices[j].X * perpindicularStack[i].X + Vertices[j].Y * perpindicularStack[i].Y);
                if (amin == null || dot < amin) amin = dot;
                if (amax == null || dot > amax) amax = dot;
            }
            for (int j = 0; j < other.Vertices.Length; j++)
            {
                dot = (int)(other.Vertices[j].X * perpindicularStack[i].X + other.Vertices[j].Y * perpindicularStack[i].Y);
                if (bmin == null || dot < bmin) bmin = dot;
                if (bmax == null || dot > bmax) bmax = dot;
            }
            if (bmin == null || bmax == null || amin == null || amax == null) 
            {
                throw new InvalidOperationException("Unable to calculate polygon intersection. Make sure both polygons are convex.");
            }
            if ((amin < bmax && amin > bmin) || (bmin < amax && bmin > amin))
            {
                continue;
            }
            else return false;
        }
        return true;
    }

    /// <summary>
    /// Returns a value that indicates whether this polygon and the specified object are equal
    /// </summary>
    /// <param name="obj">The object to compare with this polygon.</param>
    /// <returns>true if this polygon and the specified object are equal; otherwise, false.</returns>
    public override readonly bool Equals(object obj) => obj is Polygon other && Equals(other);

    /// <summary>
    /// Returns a value that indicates whether this polygon and the specified polygon are equal.
    /// </summary>
    /// <param name="other">The polygon to compare with this polygon.</param>
    /// <returns>true if this polygon and the specified polygon are equal; otherwise, false.</returns>
    public readonly bool Equals(Polygon other) => Vertices == other.Vertices;

    /// <summary>
    /// Returns the hash code for this polygon.
    /// </summary>
    /// <returns>The hash code for this polygon as a 32-bit signed integer.</returns>
    public override readonly int GetHashCode() => HashCode.Combine(Vertices);

    /// <summary>
    /// Returns a value that indicates if the polygon on the left hand side of the equality operator is equal to the
    /// polygon on the right hand side of the equality operator.
    /// </summary>
    /// <param name="lhs">The polygon on the left hand side of the equality operator.</param>
    /// <param name="rhs">The polygon on the right hand side of the equality operator.</param>
    /// <returns>true if the two polygons are equal; otherwise, false.</returns>
    public static bool operator ==(Polygon lhs, Polygon rhs) => lhs.Equals(rhs);

    /// <summary>
    /// Returns a value that indicates if the polygon on the left hand side of the inequality operator is not equal to the
    /// polygon on the right hand side of the inequality operator.
    /// </summary>
    /// <param name="lhs">The polygon on the left hand side of the inequality operator.</param>
    /// <param name="rhs">The polygon on the right hand side fo the inequality operator.</param>
    /// <returns>true if the two polygon are not equal; otherwise, false.</returns>
    public static bool operator !=(Polygon lhs, Polygon rhs) => !lhs.Equals(rhs);

}