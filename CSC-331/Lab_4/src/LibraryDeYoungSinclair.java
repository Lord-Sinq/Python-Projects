/**
 * @purpose to creat a library to pass through the book class
 * @author Sinclair DeYoung
 * @date 15.09.2023
 * @section CSC 331-003
 */
import java.util.Scanner;
public class LibraryDeYoungSinclair {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // ask for books
        System.out.print("Enter the number of books:");
        int numBooks = scanner.nextInt();
        // Create an array of book objects based on user input
        Book[] library = new Book[numBooks];
        scanner.nextLine();
        // make the array with book info
        for(int i = 0; i < numBooks; i++){
            System.out.println("Enter detail for Book #" + (i + 1) + ":");
            System.out.print("Title: ");
            String title = scanner.nextLine();
            System.out.print("Author: ");
            String author = scanner.nextLine();
            System.out.print("Cover(paperback or hardcover): ");
            String cover = scanner.nextLine();
            System.out.print("Numbers of pages: ");
            int pages = scanner.nextInt();
            System.out.print("Copyright year: ");
            int copyrights = scanner.nextInt();

            // create a book object and add it to the library array
            library[i] = new Book(title, author, cover, pages, copyrights, 0.0);
            scanner.nextLine();
        }
        // displaying the library
        System.out.println("\nLibrary: ");
        System.out.println("--------------------------------------------------------");
        System.out.printf("%-20s %-20s %-10s %-10s %-10s %-15s%n", "Title", "Author", "Cover", "Pages", "Copyright", "Read time");
        for(Book book : library){
            float readTime = book.calculateReadTime(250);
            System.out.printf("%-20s %-20s %-10s %-10d %-10d %-15.2f%n", book.getTitle(), book.getAuthor(), book.getCover(), book.getPages(), book.getCopyrights(), book.getReadTime());
        }
        System.out.println("--------------------------------------------------------");

        scanner.close();
    }

}
