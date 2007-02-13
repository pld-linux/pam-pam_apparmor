%define		modulename pam_apparmor
%define		_ver 2.0
%define		_svnrel 126
Summary:	PAM module to add AppArmor change_hat functionality
Summary(pl.UTF-8):	Moduł PAM dodający funkcjonalność AppArmor change_hat
Name:		pam-%{modulename}
Version:	%{_ver}.%{_svnrel}
Release:	1
License:	GPL
Group:		Base
Source0:	http://forgeftp.novell.com/apparmor/Development%20-%20September%20snapshot/%{modulename}-%{_ver}-%{_svnrel}.tar.gz
# Source0-md5:	018ebf7d4618760b8b4a3b34b84da9e6
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
BuildRequires:	libapparmor-devel
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pam_apparmor module provides the means for any PAM applications
that call pam_open_session() to automatically perform an AppArmor
change_hat operation in order to switch to a user-specific security
policy.

%description -l pl.UTF-8
Moduł pam_apparmor daje możliwość każdej aplikacji PAM wywołującej
pam_open_session() automatycznie wykonać operację AppArmor change_hat
w celu przełączenia na specyficzną dla użytkownika politykę
bezpieczeństwa.

%prep
%setup -q -n %{modulename}-%{_ver}

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -D pam_apparmor.so $RPM_BUILD_ROOT/%{_lib}/security/pam_apparmor.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_apparmor.so
