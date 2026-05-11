package org.example;

import java.util.Scanner;
import java.util.List;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in);
             SessionFactory factory = new Configuration()
                     .configure("hibernate.cfg.xml")
                     .addAnnotatedClass(Category.class)
                     .addAnnotatedClass(Book.class)
                     .buildSessionFactory()) {

            int c = 0;
            while (c != 6) {
                System.out.println("\n--- Book Store Inventory ---");
                System.out.println("1. Print all books");
                System.out.println("2. Add a book");
                System.out.println("3. Delete a book");
                System.out.println("4. Edit a book price");
                System.out.println("5. Insert a trial book loadout");
                System.out.println("6. Exit");
                System.out.print("Enter c: ");

                c = sc.nextInt();
                sc.nextLine();

                if (c == 6)
                    break;
                try (Session session = factory.openSession()) {
                    Transaction tx = session.beginTransaction();

                    try {
                        switch (c) {
                            case 1:
                                // print all books
                                List<Book> books = session.createQuery("from Book", Book.class).list();
                                if (books.isEmpty()) System.out.println("No books in inventory.");
                                for (Book b : books) {
                                    System.out.println(b.getIsbn() + " | " + b.getTitle() + " | $" + b.getPrice());
                                }
                                break;

                            case 2:
                                // add book
                                System.out.print("Enter ISBN: ");
                                String isbn = sc.nextLine();
                                System.out.print("Enter Title: ");
                                String title = sc.nextLine();
                                System.out.print("Enter Price: ");
                                double price = sc.nextDouble();

                                Book newBook = new Book();
                                newBook.setIsbn(isbn);
                                newBook.setTitle(title);
                                newBook.setPrice(price);

                                session.persist(newBook);
                                System.out.println("Book added!");
                                break;

                            case 3:
                                // delete book
                                System.out.print("Enter ISBN to delete: ");
                                String delIsbn = sc.nextLine();
                                Book toDelete = session.get(Book.class, delIsbn);
                                if (toDelete != null) {
                                    session.remove(toDelete);
                                    System.out.println("Book deleted.");
                                } else {
                                    System.out.println("Book not found.");
                                }
                                break;

                            case 4:
                                // edit price
                                System.out.print("Enter ISBN to edit: ");
                                String editIsbn = sc.nextLine();
                                Book toEdit = session.get(Book.class, editIsbn);
                                if (toEdit != null) {
                                    System.out.print("Enter new price: ");
                                    toEdit.setPrice(sc.nextDouble());
                                    session.merge(toEdit);
                                    System.out.println("Price updated.");
                                } else {
                                    System.out.println("Book not found.");
                                }
                                break;

                            case 5:
                                // insert trial
                                Category cat = new Category();
                                cat.setName("Technology");

                                Book b = new Book();
                                b.setIsbn("100");
                                b.setTitle("Trial 1");
                                b.setPrice(45.00);

                                b.setCategory(cat);
                                cat.getBooks().add(b);

                                session.persist(cat);
                                System.out.println("Trial data (Category + Book) loaded!");
                                break;

                            default:
                                System.out.println("Please enter a proper c!!!");
                                break;
                        }
                        tx.commit();
                    } catch (Exception e) {
                        if (tx != null) tx.rollback();
                        System.err.println("Transaction failed: " + e.getMessage());
                    }
                }
            }
            System.out.println("Application closed.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}