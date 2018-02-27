import javax.swing.text.Document;
import javax.swing.text.rtf.RTFEditorKit;
import javax.swing.text.BadLocationException;
import java.io.*;
import java.util.*;
import java.net.URL;

public class rtfparser{

  public static void main(String[] args){
    String name = "ncdsessay-1-n10014t.rtf";
    parseRTF();


  }

  public static void parseRTF()
  {
    // URL location = rtfparser.class.getProtectionDomain().getCodeSource().getLocation();
    // System.out.println(location.getFile());
    String myDirectoryPath = "/Users/abigailatchison/Documents/MLAT/Health_Essay/full_essays";
    File dir = new File(myDirectoryPath);
    File[] directoryListing = dir.listFiles();
    if (directoryListing != null) {
    for (File child : directoryListing) {
      String filename = child.getName();
      System.out.println(filename);
      writetxt(readrtf("/Users/abigailatchison/Documents/MLAT/Health_Essay/full_essays/"+filename), filename.substring(0,filename.length()-4)+".txt");
    }
    } else {
    // Handle the case where dir is not really a directory.
    // Checking dir.isDirectory() above would not be sufficient
    // to avoid race conditions with another process that deletes
    // directories.
    }

  }

  public static void writetxt(String[] lines, String filename)
  {
    try(PrintWriter out = new PrintWriter(filename) ){
      for(int i = 2; i<lines.length-1; ++i)
      {
        String line = lines[i];
        line = line.replaceAll("\\[.*?\\] ?", "");
        line = line.replaceAll("\\(.*?\\) ?", "");
        out.println(line);
      }
    }catch(FileNotFoundException e)
    {
      System.out.println("File not found:" + filename);
    }
  }

  public static String[] readrtf(String fileloc)
  {
    FileInputStream stream;
    try{
      stream = new FileInputStream(fileloc);
      RTFEditorKit kit = new RTFEditorKit();
      Document doc = kit.createDefaultDocument();
      try{
        kit.read(stream, doc, 0);
      }catch(BadLocationException|IOException e){
        System.out.println(e);
      }
      String plainText = "";
      try{
        plainText = doc.getText(0, doc.getLength());
      }catch(BadLocationException e){
        System.out.println(e);
      }
      return plainText.split("\\n");
    }catch(FileNotFoundException e){
      System.out.println("Cannot find file: " + fileloc);
    }

    return new String[1];
  }
}
