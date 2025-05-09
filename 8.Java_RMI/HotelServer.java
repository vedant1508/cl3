import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class HotelServer extends UnicastRemoteObject implements HotelInterface {

    private static final long serialVersionUID = 1L;
    private Set<String> bookedGuests;

    protected HotelServer() throws RemoteException {
        super();
        bookedGuests = new HashSet<>();
    }

    @Override
    public synchronized String bookRoom(String guestName) throws RemoteException {
        if (bookedGuests.contains(guestName)) {
            String message = "Room already booked for " + guestName;
            System.out.println("[Server Log] " + message);
            return message;
        }
        bookedGuests.add(guestName);
        String message = "Room successfully booked for " + guestName;
        System.out.println("[Server Log] " + message);
        return message;
    }

    @Override
    public synchronized String cancelBooking(String guestName) throws RemoteException {
        if (bookedGuests.remove(guestName)) {
            String message = "Booking canceled for " + guestName;
            System.out.println("[Server Log] " + message);
            return message;
        } else {
            String message = "No booking found for " + guestName;
            System.out.println("[Server Log] " + message);
            return message;
        }
    }

    public static void main(String[] args) {
        try {
            HotelServer obj = new HotelServer();
            Registry registry = LocateRegistry.createRegistry(1099); // default RMI port
            registry.rebind("HotelService", obj);
            System.out.println("[Server Log] Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// javac *.java
// java HotelServer
// New Terminal 
// java HotelClient
