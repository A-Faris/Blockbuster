import {
  assertEquals,
  assertThrows
} from 'https://deno.land/std/testing/asserts.ts'
import { Video, Customer, VideoStore, Rental, DVD, VendingMachine } from './blockbuster_oop.js'

Deno.test('Customer.name', () => {
  const john = new Customer('John', 'Smith', '24/01/1980')
  assertEquals(john.name, 'John Smith')
})

// Fill out more tests below :)! assertEquals and assertThrows should be all you need, but there
// are "fancier" asserts available too, see https://deno.land/manual/testing/assertions
