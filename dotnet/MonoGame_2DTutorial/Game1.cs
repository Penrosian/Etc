using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using MonoGame_GameLibrary;

namespace MonoGame_2DTutorial;

public class Game1 : Core
{
    private Texture2D _logo;

    public Game1() : base("Dungeon Slime", 1280, 720, false)
    {
        Content.RootDirectory = "Content";
        IsMouseVisible = true;
    }

    protected override void Initialize()
    {
        // TODO: Add your initialization logic here

        base.Initialize();
    }

    protected override void LoadContent()
    {
        _logo = Content.Load<Texture2D>("images/logo");
    }

    protected override void Update(GameTime gameTime)
    {
        if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
            Exit();

        // TODO: Add your update logic here

        base.Update(gameTime);
    }

    protected override void Draw(GameTime gameTime)
    {
        GraphicsDevice.Clear(Color.CornflowerBlue);

        SpriteBatch.Begin();
        SpriteBatch.Draw(
            _logo, 
            new Vector2(
                Window.ClientBounds.Width, 
                Window.ClientBounds.Height) 
            * 0.5f, 
            null,
            Color.White,
            0.0f,
            Helper.GetTextureCenter(_logo),
            1.0f,
            SpriteEffects.None,
            0.0f
        );
        SpriteBatch.End();

        base.Draw(gameTime);
    }
}
