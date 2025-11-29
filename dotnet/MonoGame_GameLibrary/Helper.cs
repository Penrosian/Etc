using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using MonoGame_GameLibrary.Graphics;

namespace MonoGame_GameLibrary
{
    public static class Helper
    {
        public static Vector2 GetTextureCenter(Texture2D texture)
        {
            return new Vector2(texture.Bounds.Width, texture.Bounds.Height) * 0.5f;
        }
        public static Vector2 GetTextureCenter(Rectangle rectangle)
        {
            return new Vector2(rectangle.Width, rectangle.Height) * 0.5f;
        }
        public static Vector2 GetTextureCenter(TextureRegion region)
        {
            return new Vector2(region.Width, region.Height) * 0.5f;
        }
    }
}