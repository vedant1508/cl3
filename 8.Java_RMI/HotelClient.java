import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            HotelInterface stub = (HotelInterface) registry.lookup("HotelService");

            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("\nHotel Booking System");
                System.out.println("1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline

                if (choice == 1) {
                    System.out.print("Enter guest name: ");
                    String name = scanner.nextLine();
                    String response = stub.bookRoom(name);
                    System.out.println(response);
                } else if (choice == 2) {
                    System.out.print("Enter guest name: ");
                    String name = scanner.nextLine();
                    String response = stub.cancelBooking(name);
                    System.out.println(response);
                } else {
                    break;
                }
            }

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
