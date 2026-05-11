package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {

        student s1 = new student();
        s1.setRollNo(102);
        s1.setsName("kumar");
        s1.setsAge(20);
        Configuration cfg = new Configuration();
        cfg.addAnnotatedClass(student.class);
        cfg.configure("hibernate.cfg.xml");
        SessionFactory sf = cfg.buildSessionFactory();
        Session session = sf.openSession();
        Transaction transaction = session.beginTransaction();

        session.persist(s1);

        transaction.commit();
        System.out.println(s1);

    }

}