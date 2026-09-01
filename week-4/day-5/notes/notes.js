console.log("hello");

setTimeout(() => {
    console.log("Ho no!")
}, 1000);

console.log("Bye");

//what is going on behind the scenes as this runs in the JS event loop

// step 1
// BOX 1: 1 7
// BOX 2: 4
// MAILBOX: empty

// step 2
// BOX 1: empty
// BOX 2: 4
// MAILBOX: empty

// step 3
// BOX 1: empty
// BOX 2: 4 -> the delivery guy
// MAILBOX: empty

// step 4
// BOX 1: empty
// BOX 2: empty
// MAILBOX: empty

// step 5
// BOX 1: empty
// BOX 2: empty
// MAILBOX: 4 <- the delivery guy

// step 6
// BOX 1: 4
// BOX 2: empty
// MAILBOX: empty

// step 6
// BOX 1: empty
// BOX 2: empty
// MAILBOX: empty





