/* This script describes the payment with the paystack API. */


const paymentForm = document.getElementById('paymentForm');
paymentForm.addEventListener("submit", payWithPaystack, false);

function payWithPaystack(e) {
  e.preventDefault();
s
  let handler = PaystackPop.setup({
    key: 'pk_test_dc6aa3d710e6cbbc56cd6918f406c328cb179ada',
    email: document.getElementById("email").value,
    amount: document.getElementById("amount").value * 100,
    //ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      let message = 'Payment complete! Reference: ' + response.reference;
      alert(message);
    }
  });

  handler.openIframe();
}


function verifyTransaction(reference) {
  fetch('/payment/verify', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ reference: reference })
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'success') {
      alert('Transaction verified successfully.');
      // Update user wallet or perform other actions
    } else {
      alert('Transaction verification failed.');
    }
  });
}

