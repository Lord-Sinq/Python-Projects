/**
 * @purpose UML project taking users book inputs from Library and
 * having setters and getters for this.
 * @author Sinclair DeYoung
 * @date 15.09.2023
 * @section CSC 331-003
 */
public class Book {
    //class attributes
    private String title;
    private String author;
    private String cover;
    private int pages;
    private int copyrights;
    private double readTime;
    //Constructor
    public Book(String title, String author, String cover, int pages, int copyright, double readTime ){
        this.title = title;
        this.author = author;
        this.cover = cover;
        this.pages = pages;
        this.copyrights = copyright;
        this.readTime = readTime;
    }
    //Accessor Methods
    public String getTitle() { return title;}
    public String getAuthor() { return author;}
    public String getCover() { return cover;}
    public int getPages() { return pages;}
    public int getCopyrights() { return copyrights;}
    public double getReadTime() { return readTime;}

    //Mutator Methods
    public void setTitle(String title) { this.title = title;}
    public void setAuthor(String author) { this.author = author;}
    public void setCover(String cover) { this.cover = cover;}
    public void setPages(int pages) { this.pages = pages;}
    public void setCopyrights(int copyrights) { this.copyrights = copyrights;}
    public void setReadTime(double readTime) { this.readTime = readTime;}

    // Normal Method to calc the time it takes to read the book
    public float calculateReadTime(int ppm){
        return (float)pages/ppm;
    }
}


