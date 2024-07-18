# Blockkbuster

## Project Overview

We'll take a trip back to the 90s to create a rental system for BlockBuster video. We'll dive into the specification of different parts of the system, but from a high level. In our system:

- Videos have a title, year of release, runtime and rental price.
- BlockBuster stores stock multiple videos for rental.
- Stores can look up videos by name.
- Customers can rent videos up to 3 videos at a time. Videos have to be rewound before being returned. Any late returns incur fines.
- Customers with significant outstanding fines can't rent videos (until their fines are paid off).

We'll implement new kinds of media (DVDs) for BlockBuster to stock and launch BlockBuster vending machines.