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
            return "Room already booked for " + guestName;
        }
        bookedGuests.add(guestName);
        return "Room successfully booked for " + guestName;
    }

    @Override
    public synchronized String cancelBooking(String guestName) throws RemoteException {
        if (bookedGuests.remove(guestName)) {
            return "Booking canceled for " + guestName;
        } else {
            return "No booking found for " + guestName;
        }
    }

    public static void main(String[] args) {
        try {
            HotelServer obj = new HotelServer();
            Registry registry = LocateRegistry.createRegistry(1099); // default port
            registry.rebind("HotelService", obj);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
// javac *.java
// java HotelServer
// New Terminal
// java HotelClient
