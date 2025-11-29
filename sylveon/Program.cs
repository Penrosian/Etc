string[] lines = File.ReadAllLines("/home/penrosian/repos/csc221/other/curses_sylveon/sylveon_big_colored.txt");

int[] white = new int[] {255, 255, 255};
int[] pink = new int[] {239, 154, 172};
int[] lightBlue = new int[] {157, 223, 250};
int[] blue = new int[] {29, 153, 243};
int[] gray = new int[] {179, 179, 179};

foreach (string line in lines) {
    string new_line = String.Join("$1", line);
    string[] segments = new_line.Split('$');
    foreach (string segment in segments) {
        if (segment.StartsWith("1")) {
            Console.Write($"\x1b[38;2;{white[0]};{white[1]};{white[2]}m{segment[1..]}\x1b[0m");
        } else if (segment.StartsWith("2")) {
            Console.Write($"\x1b[38;2;{pink[0]};{pink[1]};{pink[2]}m{segment[1..]}\x1b[0m");
        } else if (segment.StartsWith("3")) {
            Console.Write($"\x1b[38;2;{lightBlue[0]};{lightBlue[1]};{lightBlue[2]}m{segment[1..]}\x1b[0m");
        } else if (segment.StartsWith("4")) {
            Console.Write($"\x1b[38;2;{blue[0]};{blue[1]};{blue[2]}m{segment[1..]}\x1b[0m");
        } else if (segment.StartsWith("5")) {
            Console.Write($"\x1b[38;2;{gray[0]};{gray[1]};{gray[2]}m{segment[1..]}\x1b[0m");
        } else {
            Console.Write(segment);
        }
    }
    Console.Write("\n");
}
// $"\x1b[38;2;{r};{g};{b}mThis text is in a custom hex color.\x1b[0m"
