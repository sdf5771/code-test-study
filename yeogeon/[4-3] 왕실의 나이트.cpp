#include <iostream>
#include <vector>

using namespace std;

struct Param {
	char c{};
	int n{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.c >> p.n;
		return is;
	}
};

using Result = int;

Result MySolution( Param param );
Result BookSolution( Param param );

int main()
{
	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;
}

Result MySolution( Param param )
{
	int x{ param.c - 'a' + 1 };
	int y{ param.n };

	Result cnt{};

	struct Pos {
		int x{}, y{};
	};

	Pos pos[8]{
		{2, 1}, {2, -1}, {-2, 1}, {-2, -1},
		{1, 2}, {-1, 2}, {1, -2}, {-1, -2}
	};

	for ( const auto& p : pos ) {
		if (
			x + p.x < 1 or
			x + p.x > 8 or
			y + p.y < 1 or
			y + p.y > 8
			)
			continue;
		++cnt;
	}

	return cnt;
}

Result BookSolution( Param param )
{
	return Result{};
}
