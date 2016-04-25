%define		modulename pam_apparmor
Summary:	PAM module to add AppArmor change_hat functionality
Summary(pl.UTF-8):	Moduł PAM dodający funkcjonalność AppArmor change_hat
Name:		pam-%{modulename}
Version:	2.10.1
Release:	1
Epoch:		1
License:	BSD or GPL
Group:		Base
Source0:	http://launchpad.net/apparmor/2.10/%{version}/+download/apparmor-%{version}.tar.gz
# Source0-md5:	c9d82e04d699b0530b12dec15136027d
URL:		http://wiki.apparmor.net/
BuildRequires:	libapparmor-devel >= 1:%{version}
BuildRequires:	pam-devel
Requires:	libapparmor >= 1:%{version}
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
%setup -q -n apparmor-%{version}

%build
%{__make} -C changehat/pam_apparmor \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	CC="%{__cc}" \
	USE_SYSTEM=1

%install
rm -rf $RPM_BUILD_ROOT

install -D changehat/pam_apparmor/pam_apparmor.so $RPM_BUILD_ROOT/%{_lib}/security/pam_apparmor.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changehat/pam_apparmor/{COPYING,README}
%attr(755,root,root) /%{_lib}/security/pam_apparmor.so
