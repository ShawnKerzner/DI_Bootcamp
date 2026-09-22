import {greetings} from "./greetings.js";
import { useChalk } from "./colorful-messages.js";
import { reading } from "./files/read-file.js";


console.log(greetings("Shawn"));
useChalk("Shawn", "Tuesday");
reading("./files/file-data.txt");



