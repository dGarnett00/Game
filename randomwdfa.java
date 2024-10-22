class Main {
  public static void main(String[] args) {
    int number = 0;

    while (number < 10){
      System.out.println("number is: " + number);
      number++;
    }
  }
}



class Main {
    public static void main(String[]){
      BankAccount account = new BankAccount();
      account.accountHolder = "bug";
      account.accountValue = 99.99;
      System.out.println(account.accountHolder);
    }
  }


  class BankAccount{
    String accountHolder;
    double accountValue;
    
  
    
  }